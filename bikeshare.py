import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print(' '*1)

    cities = ['chicago','new york city','washington']

    city = str(input('Would you like to see data for Chicago, New York City, or Washington? ').lower())
    while(city not in cities):
        city = str(input('Error - Please re-enter one of the cities Chicago, New York City, or Washington? ').lower())

    # get user input for month (all, january, february, ... , june)
    print(' '*1)
    month = str(input('Would you like to see data for January, February, March, April, May, June or all? ').lower())

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print(' '*1)
    day = str(input('Would you like to see data for Monday, Tuesday, ... Sunday or all? ').lower())

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['hour'] =  df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ',common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week is: ',common_day_of_week)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is: ',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ',common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ',common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start & End Station'] = df['Start Station'] + ' to ' + df['End Station']
    common_start_end_station = df['Start & End Station'].mode()[0]
    print('The most frequent combination of start and end station is: ',common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('The total travel time is: ',total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The average travel time is: ',mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Total number of user types:')
    print(user_types)

    print(' ')

    # Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('Counts of gender:')
        print(count_gender)
    else:
        print('Gender column not found')

    print(' ')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth: ',earliest_birth)
        print('Most recent year of birth: ',recent_birth)
        print('Most common year of birth: ',common_birth)
    else:
        print('Birth Year column not found')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    start=0
    while True:
        raw_data=input('Would you like to see five rows of raw data? Yes or No? ').lower()
        if raw_data == 'yes':
            print(df[start:start+5])
            start +=5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
