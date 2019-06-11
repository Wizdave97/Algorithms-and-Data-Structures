def party_planner(num_people,num_cookies):
    try:
        message='Each person gets {} and {} cookies remain'.format(num_cookies//num_people,num_cookies%num_people)
        return message
    except ZeroDivisionError as e:
        print('\n{} :Zero is not a valid input'.format(e))
    except ValueError:
        print('\nThe values inserted must be whole numbers')
    except TypeError:
        print('\nWrong input type')
    except Exception as e:
        print('Exception raised: {}'.format(e))
    finally:
        print('\nArguments {} people and {} cookies'.format(num_people,num_cookies))
print(party_planner(9,30))
