from ovos_plugin_manager.templates.g2p import Grapheme2PhonemePlugin, OutOfVocabulary
import pronouncing


class CmuDictPlugin(Grapheme2PhonemePlugin):

    def get_arpa(self, word, lang, ignore_oov=False):
        if lang.lower().startswith("en"):
            phones = pronouncing.phones_for_word(word)
            if phones:
                return phones[0].split(" ")
        if ignore_oov:
            return None
        raise OutOfVocabulary

    @property
    def available_languages(self):
        """Return languages supported by this G2P implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return {"en"}


# sample valid configurations per language
# "display_name" and "offline" provide metadata for UI
# "priority" is used to calculate position in selection dropdown
#       0 - top, 100-bottom
# all keys represent an example valid config for the plugin
CmuDictConfig = {
    "en-us": [
        {"lang": "en-us",
         "display_name": "CmuDict",
         "priority": 80,
         "native_alphabet": "ARPA",
               "durations": False,
         "offline": True}
    ]
}
