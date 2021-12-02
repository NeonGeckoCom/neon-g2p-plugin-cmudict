#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'ovos-g2p-cmudict-plugin=ovos_g2p_cmudict_plugin:CmuDictPlugin'
setup(
    name='ovos-g2p-cmudict-plugin',
    version='0.0.1',
    description='A utterance2phoneme plugin ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/g2p-cmudict-plugin',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='bsd3',
    packages=['ovos_g2p_cmudict_plugin'],
    zip_safe=True,
    keywords='mycroft plugin utterance phoneme',
    entry_points={'ovos.plugin.g2p': PLUGIN_ENTRY_POINT}
)
