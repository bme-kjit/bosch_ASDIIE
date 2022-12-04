from argparse import ArgumentParser


class CustomArgParser:

    def __init__(self, config):
        self.config = config

    def get_parsed_config(self):
        arg_parser = ArgumentParser()
        arg_parser.add_argument("--gui", type=str, default=self.config.gui)
        arg_parser.add_argument("--map_width", type=int, default=self.config.map_width)
        arg_parser.add_argument("--map_height", type=int, default=self.config.map_height)
        arg_parser.add_argument("--difficulty", type=float, default=self.config.difficulty)
        arg_parser.add_argument("--num_pellets", type=int, default=self.config.num_pellets)
        arg_parser.add_argument("--num_ghosts", type=int, default=self.config.num_ghosts)
        arg_parser.add_argument("--base_score", type=int, default=self.config.base_score)
        arg_parser.add_argument("--step_confidence", type=float, default=self.config.step_confidence)
        parsed_args = arg_parser.parse_args()

        parsed_args_dict = vars(parsed_args)
        self_config_dict = vars(self.config)

        for item in self_config_dict.keys():
            if item not in parsed_args_dict.keys():
                parsed_args_dict[item] = self_config_dict[item]

        return parsed_args
