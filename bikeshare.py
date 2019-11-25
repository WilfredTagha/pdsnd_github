import time, datetime
import pandas as pd
import numpy as np
import statistics as st

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ('january', 'febuary', 'march', 'april', 'may', 'june', 'all')
WEEKS = ('monday', 'tuesday', 'wednesday', 'thursday', 'friaday', 'saturday', 'sunday', 'all')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Please all the information you type in should be in lower case else you will be asked to enter a valid one.')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inpts
    city = input('Which city do you want to explore its data? \n chicago? \n new york city?\n or washington? ')
    while city not in CITY_DATA:
        city = input('please enter a valid city name \n it must be amongst the three listed above and spelt as they are ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Do you have a desired month? \n if Yes then write the month name \n but if not, type "all"  ')
    while month not in MONTHS:
        month = input('Please input a valid month or type "all"\n')
    day = input('Do you have a desired day? \n If yes write the name \n but if not, type "all"  ')
    while day not in WEEKS:
        day = input('Please input a valid day of the week\nnot integers nor short form  ')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    print('you have choosen city: ' + city + '\n month: ' + month + '\n and day: ' +day)
    return city, month, day


def load_data(city, month, day):

# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.second

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
    #print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Which month is most common?')
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        popular_month = "january"
    elif popular_month == 2:
        popular_month = "february"
    elif popular_month == 3:
        popular_month = "march"
    elif popular_month == 4:
        popular_month = "april"
    elif popular_month == 5:
        popular_month = "may"
    elif popular_month == 6:
        popular_month = "june"


    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    print('What is the most popular hour week day?\n')
    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most common day of the week:', popular_day_of_week)

    #TO DO: display the most popular start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    print('What is the most popular hour of the day?\n')
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)





    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('What is the popular start station?\n')
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular start station: ', popular_start_station)

    # TO DO: display most commonly used end station
    print('What is the most popular end station?\n')
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('What is the most common trip from start to end?\n')
    popular_star_and_end_station = (df['Start Station']+' and ends in '+df['End Station']).mode()[0]
    print('The most common trip is that wich starts at ', popular_star_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()




    # TO DO: display total travel time and mean time of Travel
    print('what is the total time of travel and the mean time of travel?\n\n')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time']  = pd.to_datetime(df['End Time'])
    right = df['End Time']-df['Start Time']
    try:
        diff = right.total_seconds()
        total = sum(diff)
        tot = int(total)
        mean = st.mean(diff)
        print('The total time in seconds is: ', tot, '\n which is still: ', str(datetime.timedelta(seconds= tot)), '\n\n\n The mean time travel is: ', mean/60,'minutes')

    except AttributeError:  # no method total_seconds
        one_second = np.timedelta64(1000000000, 'ns')
        # use nanoseconds to get highest possible precision in output
        diff = right / one_second
        total = sum(diff)
        tot = int(total)
        mean =  st.mean(diff)
        print('The total time in seconds is: ', tot, '\n which is still: ', str(datetime.timedelta(seconds= tot)), '\n\n\n The mean time travel is: ', mean/60,'minutes')
        return tot



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)







def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('What are the counts of each user type?\n')
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender,provide user data if available
    if 'Gender' in df:
        print('\n\nWhat are the counts of each Gender?\n')
        gender_count = df['Gender'].value_counts()
        print(gender_count, '\n\n')
        try:


            earliest_year_of_birth = df['Birth Year'].sort_values(ascending = False)[0]
            most_recent_year_of_birth = df['Birth Year'].sort_values()[0]
            most_common_year_of_birth = df['Birth Year'].mode()[0]
            print('What are the earliest, most recent, and most common year of birt?\n')
            print('\nThe earliest year of birth is: ', earliest_year_of_birth)
            print('\nThe most recent year of birth is: ', most_recent_year_of_birth)
            print('\nThe most common year of birth is: ',  most_common_year_of_birth)

        except:
            print('-'*40)
    else:
        print('User data is only available for New York City and Chicago')
        print('\n But washington has hours\n')
        print('What are the earliest, most recent, and most common hour?\n')
        earliest_hour = df['hour'].sort_values(ascending = False)[0]
        latest_hour = df['hour'].sort_values()[0]
        most_common_hour = df['hour'].mode()[0]
        print('\nThe earliest hour is: ', earliest_hour)
        print('\nThe latest hour is: ', latest_hour)
        print('\nThe most common hour is: ', most_common_hour)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    #Displays rows of raw data in groups of fives for as many  groups as the user wants
    print('\nCalculating Raw data...\n')
    start_time = time.time()
    ans = input('Would you like to see 5 lines of Raw_data? if not, type "no" ')
    a= 0

    while ans != 'no':
        b= a+5
        print(df.iloc[a:b])
        a+=5
        ans = input('Would you like to see 5 more lines of raw data?')

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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
