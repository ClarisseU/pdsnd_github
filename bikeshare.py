import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("which city would you like to filter? New York, Chicago or Washington\n").lower().title()
        if city not in ('New York','Washington','Chicago'):
            print('please, enter the cities between Chicago, New York and Washington')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n Kindly, enter the month you'd like to filter by..\n January, February, March, April, May, June or 'all' to view all\n").lower().title()
        if month not in('January','February','March','April','May','June', 'all'):
            print("please enter a months From January to June or 'all' to view all")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Please, Enter the following days: Sunday, Monday, Tuesday, Wednesday, Thursady, Friday, Saturday\n or type 'all' if you want to check all days\n").lower().title()
        if day not in ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','all'):
            print("\n please, try again.")
            continue
        else:
            break

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
    #load data file into DataFrame
    df = pd.read_csv(CITY_DATA[city.lower()])

    #convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extracting month and day of the week from 'Start Time' to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    #filter by month
    if month != 'all':
#         months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = month.index(month)+1
    
        #Filter by month to create a new Data Frame
        df = df[df['month'] == month]

    if day != 'all':
        #filter by the day of week
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("\n The Most Common Month: ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Common Day: ', popular_day)

    # TO DO: display the most common start hour
   
    popular_hour = df['Start Hour'].mode()[0]
    print('\nMost Common Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("\nMost commonly used start station: ", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("\nMost commonly used end station: ", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print("\nMost commonly used start station is:", start_station,"and the most commonly used end station is: ",end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("\nThe total travel time in days: ", total_travel_time/86400)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe Mean travel time in minutes: ", mean_travel_time/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nUser Types: ", user_types)

    # TO DO: Display counts of gender
    try: 
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:', gender_types)
    except KeyError:
        print('\n No data available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = df['Birth Year'].min()
        print('\n Earliest Year: ',Earliest_Year)
    except KeyError:
        print("\n No data available")
        
    try:
        Most_Recent_Year = df['Birth Year'].max()
        print("\n The most recent year: ", Most_Recent_Year)
    except:
        print("\n No data available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        step=1
        begin=0
        end=5
        
        while(step == 1):
            step=int(input("\n Do you want to review individual trip data? Type 1 or 2 \n1:True \n2:False"))
            while((step != 1) and (step != 2)):
                step=int(input("Not a valid input. Please, try again"))
            print(df.iloc[begin:end])
            begin+=5
            end+=5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
