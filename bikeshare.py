import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("choose the city you need from(chicago, new york city, washington) : ").lower()
        if city not in CITY_DATA:
            print("The city does not exist")
        else:
            break

    while True:
        month = input(
            "choose the month you need from january to june \n if you need to see all months type  (all)").lower()
        our_months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != 'all' and month not in our_months:
            print("he month does not exist")
        else:
            break

    while True:
        day = input("choose the day you need \n if you need to see all days type (all)").lower()
        our_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if day != 'all' and day not in our_days:
            print("The day does not exist")
        else:
            break
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['the_day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['the_day'] == day.title()]
    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    the_most_common_month = df['month'].mode()[0]
    print("the most common month is : ", the_most_common_month)
    the_most_common_day = df['the_day'].mode()[0]
    print("the most common day is : ", the_most_common_day)
    the_most_common_hour = df['hour'].mode()[0]
    print("the most common hour is : ", the_most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    most_start_station = df['Start Station'].mode()[0]
    print("The most start station is: ", most_start_station)
    most_end_station = df['End Station'].mode()[0]
    print("The most end station is: ", most_end_station)
    most_frequent_trip = (df['Start Station'] + "--" + df['End Station'])
    print("the most frequent combination of start station and end station trip is ", most_frequent_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    start_time = time.time()
    print('\nCalculating Trip Duration...\n')
    dtime = df['Trip Duration'].sum()
    print("Total Time is: ", dtime)
    time_mean = df['Trip Duration'].mean()
    print("Time mean is: ", time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print("User types counts is : ", df['User Type'].value_counts())

    if 'Gender' in df:
        print("User Gender counts is : ", df['Gender'].value_counts())

    if 'Birth Year' in df:
        the_earlist_year = int(df['Birth Year'].min())
        print("The earlist year is : ", the_earlist_year)
        the_recent_year = int(df['Birth Year'].max())
        print("The recent year is : ", the_recent_year)
        the_common_year = int(df['Birth Year'].mode()[0])
        print("The common year is : ", the_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
