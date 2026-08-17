import markdown
from langchain_core.tools import tool
import nh3

@tool
def markdown_to_html(markdown_text: str) -> str:
    """
    Convert a Markdown string into a formatted HTML document.
    Use this to prepare email bodies or newsletters before sending them.
    """
    raw_html = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code', 'sane_lists'])
    safe_html = nh3.clean(raw_html)

    html_document = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333333; max-width: 650px; margin: 0 auto; padding: 20px; background-color: #fcfcfc;">

        <div style="background-color: #ffffff; padding: 30px; border-radius: 8px; border: 1px solid #e0e0e0;">

            <!-- Header -->
            <div style="border-bottom: 2px solid #2c3e50; padding-bottom: 15px; margin-bottom: 25px;">
                <h1 style="color: #2c3e50; margin: 0; font-size: 24px;">Northwind Traders</h1>
                <p style="color: #7f8c8d; font-size: 14px; margin: 5px 0 0 0; text-transform: uppercase; letter-spacing: 1px;">Wholesale Gourmet Dispatch</p>
            </div>

            <!-- Main Content -->
            <div style="font-size: 15px;">
                {safe_html}
            </div>

            <!-- Signature Block -->
            <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #eeeeee; font-size: 14px; color: #555555;">
                <p style="margin: 0 0 5px 0;">Warm regards,</p>
                <p style="margin: 0;">
                    <strong>Nancy</strong><br>
                    Account Representative<br>
                    <em>Northwind Traders</em><br>
                    <span style="color: #7f8c8d; font-size: 12px;">Premium B2B Specialty Foods & Wholesale</span>
                </p>
            </div>

        </div>

    </body>
    </html>"""
    return html_document