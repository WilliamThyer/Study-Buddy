from gooey import Gooey, GooeyParser

@Gooey(program_name='Study Buddy', image_dir='./icons')
def main():
    min_list = ['1','2','5','10','15','30','45','60']
    parser = GooeyParser(description="The study buddy you love to hate")
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