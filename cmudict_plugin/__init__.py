from ovos_plugin_manager.templates.phonemes import Grapheme2PhonemePlugin
import pronouncing


class CmuDictPlugin(Grapheme2PhonemePlugin):

    def get_arpa(self, word, lang):
        if lang.lower().startswith("en"):
            phones = pronouncing.phones_for_word(word)
            if phones:
                return phones[0] \
                    .replace("9", "")\
                    .replace("8", "")\
                    .replace("7", "")\
                    .replace("6", "")\
                    .replace("5", "")\
                    .replace("4", "")\
                    .replace("3", "")\
                    .replace("2", "")\
                    .replace("1", "")\
                    .replace("0", "").split(" ")
        return None

