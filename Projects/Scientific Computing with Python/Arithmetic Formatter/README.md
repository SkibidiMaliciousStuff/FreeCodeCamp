<section id="description">
<p>Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="python code example"><code class="language-py">  <span class="token number">235</span>
<span class="token operator">+</span>  <span class="token number">52</span>
<span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>
</code></pre>
<p>Finish the <code>arithmetic_arranger</code> function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to <code>True</code>, the answers should be displayed.</p>
<h2>Example</h2>
<p>Function Call:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="python code example"><code class="language-py">arithmetic_arranger<span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token string">"32 + 698"</span><span class="token punctuation">,</span> <span class="token string">"3801 - 2"</span><span class="token punctuation">,</span> <span class="token string">"45 + 43"</span><span class="token punctuation">,</span> <span class="token string">"123 + 49"</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
</code></pre>
<p>Output:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="python code example"><code class="language-py">   <span class="token number">32</span>      <span class="token number">3801</span>      <span class="token number">45</span>      <span class="token number">123</span>
<span class="token operator">+</span> <span class="token number">698</span>    <span class="token operator">-</span>    <span class="token number">2</span>    <span class="token operator">+</span> <span class="token number">43</span>    <span class="token operator">+</span>  <span class="token number">49</span>
<span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>    <span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>    <span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>    <span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>
</code></pre>
<p>Function Call:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="python code example"><code class="language-py">arithmetic_arranger<span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token string">"32 + 8"</span><span class="token punctuation">,</span> <span class="token string">"1 - 3801"</span><span class="token punctuation">,</span> <span class="token string">"9999 + 9999"</span><span class="token punctuation">,</span> <span class="token string">"523 - 49"</span><span class="token punctuation">]</span><span class="token punctuation">,</span> <span class="token boolean">True</span><span class="token punctuation">)</span>
</code></pre>
<p>Output:</p>
<pre class="language-py" tabindex="0" role="region" aria-label="python code example"><code class="language-py">  <span class="token number">32</span>         <span class="token number">1</span>      <span class="token number">9999</span>      <span class="token number">523</span>
<span class="token operator">+</span>  <span class="token number">8</span>    <span class="token operator">-</span> <span class="token number">3801</span>    <span class="token operator">+</span> <span class="token number">9999</span>    <span class="token operator">-</span>  <span class="token number">49</span>
<span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>    <span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>    <span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>    <span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>
  <span class="token number">40</span>     <span class="token operator">-</span><span class="token number">3800</span>     <span class="token number">19998</span>      <span class="token number">474</span>
</code></pre>
<h2>Rules</h2>
<p>The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will <strong>return</strong> a <strong>string</strong> that describes an error that is meaningful to the user.</p>
<ul>
<li>Situations that will return an error:
<ul>
<li>If there are <strong>too many problems</strong> supplied to the function. The limit is <strong>five</strong>, anything more will return:
<code>'Error: Too many problems.'</code></li>
<li>The appropriate operators the function will accept are <strong>addition</strong> and <strong>subtraction</strong>. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
<code>"Error: Operator must be '+' or '-'."</code></li>
<li>Each number (operand) should only contain digits. Otherwise, the function will return:
<code>'Error: Numbers must only contain digits.'</code></li>
<li>Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
<code>'Error: Numbers cannot be more than four digits.'</code></li>
</ul>
</li>
<li>If the user supplied the correct format of problems, the conversion you return will follow these rules:
<ul>
<li>There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).</li>
<li>Numbers should be right-aligned.</li>
<li>There should be four spaces between each problem.</li>
<li>There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)</li>
</ul>
</li>
</ul>
<p>Note: open the browser console with F12 to see a more verbose output of the tests.</p>
</section>