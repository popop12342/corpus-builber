from corpus_builder.rule import Rule
from corpus_builder.grammar import Grammar
from corpus_builder.builder import CorpusBuilder

grammar = Grammar([
    Rule('<intent>', ('<make_update_sentence>', '<setup_printer_sentence>', '<shutdown_computer_sentence>', '<software_recommendation_sentence>', '<none_sentence>')),
    Rule('<make_update_sentence>', ['<update_predicate> ', 'from ', '<ubuntu_version> ', 'to ', '<ubuntu_version> ', '<question_mark_op>']),
    Rule('<setup_printer_sentence>', ['<printer_predicate> ', '<printer> ', '<ubuntu_version_op> ', '<wireless_op>', '<question_mark_op>']),
    Rule('<shutdown_computer_sentence>', ['<shutdown_predicate> ', '<shutdown_condition>', '<ubuntu_version_op>', '<question_mark_op>']),
    Rule('<software_recommendation_sentence>', ['<question_pronoum> ', '<software_type> ', '<recommendation_predicate> ', '<ubuntu_op> ', '<question_mark_op>']),
    Rule('<none_sentence>', ['<general_question> ', '<general_goal> ', '<question_mark_op>']),
    Rule('<question_pronoum>', ('what', 'which', 'how', '')),
    Rule('<software_type>', ['<software_qualifier> ', '<recommendation_connector> ', '<software_objective> ', '<file_type>']),
    Rule('<recommendation_connector>', ('for', 'to')),
    Rule('<software_qualifier>', ('IDE', 'GUI viewer', 'tool', 'editor', 'client', 'generator')),
    Rule('<software_objective>', ('edit', 'crop', 'delete', 'crete', 'download', 'host', 'diagnostic', 'monitor', 'analyse', 'sort', 'matching', 'plotting', 'embed', 'cut', 'read')),
    Rule('<file_type>', ('text', 'audio', 'video', 'torrent', 'Word', 'Powerpoint', 'Excel', 'tables', 'database', 'regex', 'string', 'SSH', 'MySQL', 'Audio/Video', 'MongoDB')),
    Rule('<recommendation_predicate>', ('exists', 'is recommended', 'you recommend', 'is used', 'I can use', '')),
    Rule('<ubuntu_op>', ('for Ubuntu', '')),
    Rule('<question_mark_op>', ('?', '')),
    Rule('<update_predicate>', ('uptate', 'updating', 'how to update Ubuntu', 'upgrade', 'upgrading', 'do you recommendo updating', 'is there any problem updating Ubuntu')),
    Rule('<ubuntu_version>', ['<version_number> ', '<bits_op>']),
    Rule('<bits_op>', ('~64 bit', '~32 bit', '')),
    Rule('<version_number>', ('<version_3_parts>', '<version_2_parts>')),
    Rule('<version_3_parts>', ['<one_op> ', '<num>', '.', '<num> ', '<num>', '.', '<num>', '<num>']),
    Rule('<version_2_parts>', ['<one_op> ', '<num>', '.', '<num> ', '<num>']),
    Rule('<one_op>', ('1', '')),
    Rule('<num>', ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')),
    Rule('<ubuntu_version_op>', ('on Ubunutu', '<aux1>', '')),
    Rule('<aux1>', ['on ', '<ubuntu_version>']),
    Rule('<printer_predicate>', ('how to setup', 'how can i install', 'install', 'setup', 'how to install drivers')),
    Rule('<printer>', ['<printer_brand_name> ', '<printer_name>']),
    Rule('<printer_brand_name>', ('HP', 'Brother', 'Cannon', 'Pantum', 'Konica', 'Panasonic')),
    Rule('<printer_name>', ('Deskjet', 'Minolta', '<printer_name_code>')),
    Rule('<printer_name_code>', ['<char> ', '<printer_name_code_op>']),
    Rule('<printer_name_code_op>', ('<printer_name_code>', '')),
    Rule('<char>', ('<num>', '<letter>')),
    Rule('<letter>', ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-')),
    Rule('<wireless_op>', ('wireless', '')),
    Rule('<shutdown_predicate>', ('how to shutdown', 'hotkey to shutdown', 'how can i shutdown', 'shutdown', 'automatic shutdown', 'what is the proper terminal-way to shutdown', 'how to shut down', 'hotkey to shut down', 'how can i shut down', 'shut down', 'automatic shut down', 'what is the proper terminal-way to shut down')),
    Rule('<shutdown_condition>', ('without extra question', 'when users are logged on', 'after specific time', 'at certain time', 'from login screen', 'after session ends', 'using keyboard', 'at terminal', 'automatically')),
    Rule('<general_question>', ('how can I', 'how to')),
    Rule('<general_goal>', ('record my screen', 'highlight in PDF', 'save to PDF', 'send to printer'))
], '<intent>')

classes = {'<intent>': ['Make Update', 'Setup Printer', 'Shutdown Computer', 'Software Recommendation', 'None']}

entities = {
    '<printer>': 'Printer',
    '<ubuntu_version>': 'UbuntuVersion',
}

builder = CorpusBuilder(grammar, classes, entities)
print(builder.create_sentence())

corpus = builder.create_corpus(100, 2)
print(corpus[:10])