{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/drawdown/" method="post" name="FormDrawdown" class="pure-form pure-form-aligned">
      {{ p_form.hidden_tag() }}
      <fieldset>
        <div class="pure-control-group">
          <input class="pure-button" type="submit" value="Add"></input>
          {{ p_form.drawdown_id }}
        </div>
        <div class="table-responsive">
          <table class="mq-table pure-table pure-table-bordered">
            <thead>
              <tr>
                <td>#</td>
                <td>Current</td>
                <td>Max</td>
                <td>Date created</td>
                <td>Date modified</td>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{{p_form.drawdown_id}}</td>
                <td>{{ p_form.drawdown_current}}</td>
                <td>{{ p_form.drawdown_max }}</td>
                <td>{{ p_form.date_modified }}</td>
                <td>{{ p_form.date_created }}</td>
                <td>
                  <input class="pure-button" type="submit" value="Save"></input> <input class="pure-button" type="submit" value="Cancel"></input>  
                </td>
              </tr>
              <tr>
                <td>
                  <input class="pure-button" type="submit" value="M"></input> <input class="pure-button" type="submit" value="D"></input>  
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </fieldset>
    </form>
  </p>
{% endblock %}
