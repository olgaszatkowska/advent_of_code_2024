from copy import deepcopy


def get_reports():
    reports = []
    with open("inputs/2.txt") as file:
        for line in file:
            map_obj = map(int, line.split())
            reports.append(list(map_obj))
            
    return reports

def is_report_safe(report):    
    is_ascending = True if report[0] < report[1] else False
    
    for i, level in enumerate(report):
        next_i = i+1
        if next_i == len(report):
            break

        difference = level - report[next_i]
        is_currently_ascending = True if difference < 0 else False
        
        if is_ascending != is_currently_ascending:
            return False

        if abs(difference) == 0 or abs(difference) > 3:
            return False

    return True


def will_remove_help(report, i):
    report_copy = deepcopy(report)
    del report_copy[i]

    return is_report_safe(report_copy)

def is_report_fixable(report):
    for i in range(len(report)):
        is_fixable = will_remove_help(report, i)
        
        if is_fixable:
            return True
    
    return False
    

def count_safe_reports(reports: list[list[int]]):
    total_safe = 0
    total_fixable_errors = 0
    for report in reports:
        is_safe = is_report_safe(report)
        if is_safe:
            total_safe+=1
        else:
            is_fixable = is_report_fixable(report)
            
            if is_fixable:
                total_fixable_errors+=1
            
        
    print(total_safe, total_safe+total_fixable_errors)
            

reports = get_reports()
count_safe_reports(reports)
