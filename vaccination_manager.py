import create_dynamic_artifacts
import create_static_artifacts
import argparse
import os

def update_artifacts():
    """
    This will get a fresh copy of the artifacts from the Need-less repository
    :return:
    """

    # make sure you have requests installed
    import requests
    
    try:
        with open("artifacts.py", "w+") as artifacts:
            artifacts.write(requests.get("https://raw.githubusercontent.com"
                                         "/G4lB1t/Need-less/master/artifacts.py").content)
    except:
        print "Unable to update artifacts\nProceeding with current knowledge"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vaccinate your Windows machine, experimental')
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-d', action='store_true')
    parser.add_argument('-a', action='store_true')
    parser.add_argument('-w', action='store_true')

    args = parser.parse_args()

    if args.w:
        update_artifacts()
    if args.s or args.a:
        create_static_artifacts.do_static_vaccination()
    if args.d or args.a:
        create_dynamic_artifacts.do_dynamic_vaccination()
