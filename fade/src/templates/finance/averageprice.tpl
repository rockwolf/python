{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/averageprice/" method="post" name="FormAveragePrice" class="pure-form pure-form-aligned">
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
  {% if p_average_price %}
  <p>Recommended contracts to buy, when using leverage: <span class="result">{{ p_average_price }}</span>.</p>
  {% else %}
  <p> Enter prices and quantities of all previous transactions for a single commodity.</p>
  <p> That information will be used to calculate the average price it has cost you so far.</p>
  <p> You can then use that value to enter in your accounting records, when determining the profit/loss value.</p>
  {% endif %}
{% endblock %}
