<section id="description">
<p>Write a function named <code>add_time</code> that takes in two required parameters and one optional parameter:</p>
<ul>
<li>a start time in the 12-hour clock format (ending in AM or PM)</li>
<li>a duration time that indicates the number of hours and minutes</li>
<li>(optional) a starting day of the week, case insensitive</li>
</ul>
<p>The function should add the duration time to the start time and return the result.</p>
<p>If the result will be the next day, it should show <code>(next day)</code> after the time. If the result will be more than one day later, it should show <code>(n days later)</code> after the time, where "n" is the number of days later.</p>
<p>If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.</p>
<p>Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.</p>
<details class="code-details" open=""><summary class="code-details-summary">Example Code</summary><pre class="language-py" tabindex="0" role="region" aria-label="python code example"><code class="language-py">add_time<span class="token punctuation">(</span><span class="token string">'3:00 PM'</span><span class="token punctuation">,</span> <span class="token string">'3:10'</span><span class="token punctuation">)</span>
<span class="token comment"># Returns: 6:10 PM</span>

add_time<span class="token punctuation">(</span><span class="token string">'11:30 AM'</span><span class="token punctuation">,</span> <span class="token string">'2:32'</span><span class="token punctuation">,</span> <span class="token string">'Monday'</span><span class="token punctuation">)</span>
<span class="token comment"># Returns: 2:02 PM, Monday</span>

add_time<span class="token punctuation">(</span><span class="token string">'11:43 AM'</span><span class="token punctuation">,</span> <span class="token string">'00:20'</span><span class="token punctuation">)</span>
<span class="token comment"># Returns: 12:03 PM</span>

add_time<span class="token punctuation">(</span><span class="token string">'10:10 PM'</span><span class="token punctuation">,</span> <span class="token string">'3:30'</span><span class="token punctuation">)</span>
<span class="token comment"># Returns: 1:40 AM (next day)</span>

add_time<span class="token punctuation">(</span><span class="token string">'11:43 PM'</span><span class="token punctuation">,</span> <span class="token string">'24:20'</span><span class="token punctuation">,</span> <span class="token string">'tueSday'</span><span class="token punctuation">)</span>
<span class="token comment"># Returns: 12:03 AM, Thursday (2 days later)</span>

add_time<span class="token punctuation">(</span><span class="token string">'6:30 PM'</span><span class="token punctuation">,</span> <span class="token string">'205:12'</span><span class="token punctuation">)</span>
<span class="token comment"># Returns: 7:42 AM (9 days later)</span>
</code></pre></details>
<p>Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.</p>
<p>Note: open the browser console with F12 to see a more verbose output of the tests.</p>
</section>
