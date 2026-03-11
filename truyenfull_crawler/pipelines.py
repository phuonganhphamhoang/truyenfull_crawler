import re

class CleanPipeline:
    def process_item(self, item, spider):
        if 'content' in item:
            text = re.sub(r"\s+", " ", item['content'])
            item['content'] = text.strip()
        return item