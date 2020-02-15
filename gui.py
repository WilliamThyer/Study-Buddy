from gooey import Gooey, GooeyParser

@Gooey()
def main():
    min_list = ['1','2','5','10','15','30','45','60']
    parser = GooeyParser(description="Study Buddy")
    parser.add_argument(
        "Timer",
        help="How many minutes do you want to stay focused for?",
        choices=min_list,
        nargs="*",
        widget="Dropdown"
    )
    
    args = parser.parse_args()
    minutes = int(args.Timer[0])
    return minutes

if __name__ == '__main__':
    minutes = main()
    print(minutes)