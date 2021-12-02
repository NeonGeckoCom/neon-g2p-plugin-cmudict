from cmudict_plugin import CmuDictPlugin


print(CmuDictPlugin().utterance2ipa("ok google", "en"))
print(CmuDictPlugin().utterance2arpa("ok google", "en"))

print(CmuDictPlugin().get_arpa("hello", lang="en"))
print(CmuDictPlugin().get_ipa("hello", lang="en"))
print(CmuDictPlugin().get_arpa("badbadword", lang="en"))
