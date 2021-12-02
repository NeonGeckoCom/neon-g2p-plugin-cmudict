from ovos_plugin_manager.g2p import Grapheme2PhonemePlugin
import pronouncing


class CmuDictPlugin(Grapheme2PhonemePlugin):

    def get_arpa(self, word, lang):
        if lang.lower().startswith("en"):
            phones = pronouncing.phones_for_word(word)
            if phones:
                return phones[0].split(" ")
        return None
