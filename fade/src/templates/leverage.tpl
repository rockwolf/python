{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/leverage/" method="post" name="FormLeveragedContracts" class="pure-form pure-form-aligned">
      {{ p_form.hidden_tag() }}
      <fieldset>
        <div class="pure-control-group">
          {{ p_form.p_contracts }}
        </div>
        <div class="pure-control-group">
          <input class="pure-button" type="submit" value="Calculate"></input> 
        </div>
      </fieldset>
    </form>
  </p>
  {% if p_leveraged_contracts %}
  <p>Recommended contracts to buy, when using leverage: {{ p_leveraged_contracts }}.</p>
  {% else %}
  <p> Use the money management page, to calculate the number of contracts to buy.</p>
  <p> If you want to use leverage, use the above form to calculate the leverage-adjusted number of contracts to use.</p>
  {% endif %}
{% endblock %}
