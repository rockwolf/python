{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/tradingjournal/" method="post" name="FormTradingJournal" class="pure-form pure-form-aligned">
      <fieldset>
        {{ p_form.hidden_tag() }}
        {{ p_form.p_trade }}
        <div class="pure-g">
        {% if p_trade_id %}
          <!-- TODO: enter form here that is used for editing -->
          <div class="pure-u-1-1">test with trade_id</div>
        {% else %}
          <!-- TODO: this needs just a readonly view of the line? -->
          <div class="pure-u-1-1">test without trade_id</div>
        {% endif %}
        </div>
        <div class="pure-control-group">
          <input class="pure-button" type="submit" value="Add"></input>
          <input class="pure-button" type="submit" value="Remove"></input>
          <input class="pure-button" type="submit" value="Update"></input>
        </div>
      </fieldset>
    </form>
  </p>
{% endblock %}
