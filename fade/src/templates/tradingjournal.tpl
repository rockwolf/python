{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/tradingjournal/" method="post" name="FormTradingJournal">
      {{ p_form.hidden_tag() }}
      {{ p_form.p_trade }}
      <table>
      {% if p_trade_id %}
        <!-- TODO: enter form here that is used for editing -->
        <tr>
          <td> test </td>
        </tr>
      {% else %}
        <!-- TODO: this needs just a readonly view of the line? -->
        <tr>
          <td> test </td>
        </tr>
      {% endif %}
      </table>
      <input type="submit" value="Add"></input>
      <input type="submit" value="Remove"></input>
      <input type="submit" value="Update"></input>
    </form>
  </p>
{% endblock %}
