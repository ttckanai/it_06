import sys
import janome
from janome.tokenizer import Tokenizer

def get_janome_version():
    return janome.__version__

def tokenize(text):
    t = Tokenizer()
    token_list = []
    janome_attrs = ["surface","part_of_speech","infl_type","infl_form",
                "base_form","reading","phonetic","node_type"]
    for token in t.tokenize(text):
        print(token)
        token_dict = {}
        for attr_name in janome_attrs:
            attr = getattr(token, attr_name)
            token_dict[attr_name] = attr
        token_list.append(token_dict)
    
    return token_list


if __name__ == "__main__":
    janome_version = get_janome_version()
    print(janome_version)
    if len(sys.argv) > 1:
        token_list = tokenize(sys.argv[1])
        print(token_list)