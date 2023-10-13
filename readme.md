HTML (Hypertext Markup Language) uses various tags to structure and format web content. Here's a list of some common HTML tags, categorized for easier reference:

1. Document Structure:
   - `<!DOCTYPE>`: Defines the document type and version.
   - `<html>`: The root element that contains all other HTML elements.
   - `<head>`: Contains meta-information about the document.
   - `<title>`: Sets the title of the web page (appears in the browser's title bar).
   - `<meta>`: Provides metadata about the document.
   - `<link>`: Specifies relationships between the current document and external resources.
   - `<style>`: Contains CSS for styling the document.
   - `<script>`: Embeds or references JavaScript code.
   - `<base>`: Specifies a base URL for relative URLs within the document.
   - `<noscript>`: Provides content for browsers that don't support JavaScript.
   - `<body>`: Contains the visible content of the web page.

2. Text Formatting:
   - `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`: Headings of different levels.
   - `<p>`: Defines a paragraph.
   - `<br>`: Inserts a line break.
   - `<hr>`: Creates a horizontal rule (line).
   - `<strong>` or `<b>`: Makes text bold.
   - `<em>` or `<i>`: Italicizes text.
   - `<u>`: Underlines text.
   - `<del>`: Represents deleted or struck-through text.
   - `<ins>`: Represents inserted text.
   - `<sup>`: Creates superscript text.
   - `<sub>`: Creates subscript text.
   - `<mark>`: Highlights text.
   - `<code>`: Represents computer code.
   - `<pre>`: Preformatted text.

3. Lists:
   - `<ul>`: Defines an unordered (bulleted) list.
   - `<ol>`: Defines an ordered (numbered) list.
   - `<li>`: Represents list items.
   - `<dl>`: Defines a description list.
   - `<dt>`: Represents a term or item name in a description list.
   - `<dd>`: Represents the description of a term in a description list.

4. Links and Anchors:
   - `<a>`: Creates hyperlinks.
   - `<href>`: Specifies the target URL.
   - `<target>`: Specifies where to open the linked document.
   - `<mailto>`: Creates email links.

5. Images and Multimedia:
   - `<img>`: Embeds images.
   - `<audio>`: Embeds audio content.
   - `<video>`: Embeds video content.
   - `<iframe>`: Embeds external web content within a frame.

6. Forms:
   - `<form>`: Defines an HTML form for user input.
   - `<input>`: Represents an input field (e.g., text, radio button, checkbox).
   - `<textarea>`: Defines a multiline text input field.
   - `<button>`: Creates a clickable button.
   - `<select>`: Defines a dropdown list.
   - `<option>`: Represents an option in a `<select>` element.
   - `<label>`: Labels form elements.

7. Tables:
   - `<table>`: Defines a table.
   - `<tr>`: Represents a table row.
   - `<th>`: Defines a table header cell.
   - `<td>`: Represents a table data cell.
   - `<caption>`: Adds a table caption.
   - `<thead>`, `<tbody>`, `<tfoot>`: Groups table sections.

8. Divisions and Sections:
   - `<div>`: A generic container for grouping elements.
   - `<section>`: Represents a thematic section of a document.
   - `<article>`: Defines an independent piece of content.
   - `<header>`, `<footer>`, `<nav>`, `<aside>`: Semantic HTML5 elements for structural purposes.

9. Comments:
   - `<!-- Comment Text -->`: Used to add comments in HTML code.

These are some of the most commonly used HTML tags

To connect JavaScript and CSS files to an HTML document, you use specific HTML tags. Here are the primary tags used for including external JavaScript and CSS files:

1. **Link Tag for CSS (in the `<head>` section):**
   ```html
   <link rel="stylesheet" type="text/css" href="styles.css">
   ```
   - `<link>` is used to link an external CSS file.
   - `rel="stylesheet"` specifies that this is a stylesheet.
   - `type="text/css"` defines the MIME type for CSS (optional).
   - `href` specifies the path to the CSS file.

2. **Script Tag for JavaScript (typically at the end of the `<body>` section):**
   ```html
   <script src="script.js"></script>
   ```
   - `<script>` is used to include an external JavaScript file.
   - `src` specifies the path to the JavaScript file.
   - The script can also be included directly within the `<script>` tags using inline JavaScript.

3. **Internal CSS (within the `<style>` tags in the `<head>` section):**
   ```html
   <style>
     /* Your CSS rules here */
   </style>
   ```
   - This allows you to include CSS directly within the HTML file.

4. **Inline JavaScript (within `<script>` tags):**
   ```html
   <script>
     // Your JavaScript code here
   </script>
   ```
   - You can write JavaScript code directly within the HTML file using `<script>` tags. This is useful for small scripts or in situations where you want to include script code inline.

5. **Async and Defer Attributes for Script Tags:**
   ```html
   <script src="script.js" async></script>
   <script src="script.js" defer></script>
   ```
   - The `async` attribute loads and executes the script asynchronously, not blocking the HTML parsing.
   - The `defer` attribute defers script execution until after the HTML has been fully parsed.

Make sure to replace "styles.css" and "script.js" with the actual file paths to your CSS and JavaScript files. Including external CSS and JavaScript files helps keep your HTML code clean and separates the structure (HTML), presentation (CSS), and behavior (JavaScript) of your web page, which is considered a best practice in web development.