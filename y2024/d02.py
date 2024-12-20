from santas_little_helpers.scraper_elf import scrape
import numpy as np

raw = scrape(2)

data = str(raw).replace("b'","")

reports = [[int(value) for value in report.split(" ")] for report in data.split("\\n")[0:-1]]


def part1(reports=reports):

    def report_steps(report):
        return [b-a for a,b in zip(report[:-1], report[1:])]

    def is_safe(report_steps):    
        if all(1 <= i <= 3 for i in report_steps) or all(-3 <= i <= -1 for i in report_steps):
            return True
        else:
            return False

    return sum(is_safe(report_steps(report)) for report in reports)



def part2(reports=reports):

    def report_steps(report):
        return [b-a for a,b in zip(report[:-1], report[1:])]

    def is_safe(report_steps):    
        if all(1 <= i <= 3 for i in report_steps) or all(-3 <= i <= -1 for i in report_steps):
            return True
        else:
            return False

    def modify_report(report):
        return [report[:i] + report[1+i:] for i in range(len(report))]
    

    modified_reports = [modify_report(report) for report in reports]

    return sum(any([is_safe(report_steps(variant)) for variant in modified_report]) for modified_report in modified_reports)
    # Alternatively modify part1 with just:
    # return sum(any([is_safe(report_steps(variant)) for variant in modified_report]) for modified_report in [[report[:i] + report[1+i:] for i in range(len(report))] for report in reports])