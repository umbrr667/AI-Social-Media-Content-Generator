def create_prompt(product, description, platform, days):
    return f"""
You are an expert Social Media Marketing Manager.

Company/Product:
{product}

Description:
{description}

Target Platform:
{platform}

Your tasks are:

1. Create ONE high-quality social media post specifically optimized for {platform}.

2. Include:
- Catchy headline
- Professional caption
- Relevant emojis
- 8-12 hashtags
- Strong Call To Action

3. Create a {days}-day content calendar.

For each day include:
- Day Number
- Content Topic
- Caption Idea

Format your response professionally.
"""