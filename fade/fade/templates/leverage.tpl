{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/leverage" method="post" name="FormLeveragedContracts">
      {{ p_form.hidden_tag() }} 
      {{ p_form.contracts }}
      <input type="submit" value="Calculate"></input>
    </form>
  </p>
  {% if p_leveraged_contracts %}
  <p>Recommended contracts to buy, when using leverage: {{ p_leveraged_contracts }}.</p>
  {% else %}
  <p> Use the money management page, to calculate the number of contracts to buy.</p>
  <p> If you want to use leverage, use the above form to calculate the leverage-adjusted number of contracts to use.</p>
  {% endif %}
{% endblock %}
