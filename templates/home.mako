<p>Welcome in mako template</p>
<ul>
    % for item in items:
        <li>${ item }</li>
    % endfor
</ul>
<%def name="hello()">
hello world
</%def>

the def: ${hello()}

