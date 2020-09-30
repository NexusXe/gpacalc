def main(scores):

    try:
        for x in scores:
            class_name = x
            weight = scores[class_name]
            class_percentage = float(weight[0])
            print('Class Name: ' + str(class_name))
            print('Class Percentage: ' + str(class_percentage))
            if len(weight) > 1:
                class_credits = float(weight[1])
                print('Class Credits: ' + str(class_credits))
            if len(weight) > 2:
                class_multiplier = float(weight[2])
                print('Class Multiplier: ' + str(class_multiplier))
    except ValueError:
        print('Unable to parse one of the recieved values. Make sure that all of the values are numbers.')


    def crunch(class_percentage, class_credits=2, class_multiplier=1):
        if class_percentage >= 93:
            grade_points = 4
        elif class_percentage >=92 and class_percent
        




scores = {
    "Math": [80.1, 2],
    "Chemistry": [92.4, 2],
    "History": [68.1, 3],
    "English": [31, 3, 1.5]
}


if __name__ == '__main__':
    main(scores)
    