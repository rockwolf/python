{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/account/" method="post" name="FormAccount">
      {{ p_form.hidden_tag() }}
      {{ p_form.p_account }}
      <p>
        <input class="pure-button" type="submit" value="Modify"></input>
     </p>
    </form>
  </p>
  {% if p_account_changed %}
  <p>New account info saved.</p>
  {% endif %}
{% endblock %}
