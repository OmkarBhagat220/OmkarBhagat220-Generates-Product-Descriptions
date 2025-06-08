from jinja2 import Template

def render_prompt(template_str, product_info):
    safe_data = {k: v if v else "Information not provided" for k, v in product_info.items()}
    template = Template(template_str)
    return template.render(**safe_data)
