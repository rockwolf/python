{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="{{url_for('control_panel.render_account', account_id=4) }}" method="post" name="FormAccount" class="pure-form pure-form-aligned">
      {{ p_form.hidden_tag() }}
      <fieldset>
        <div class="pure-control-group">
    p_form.account_id: {{p_form.account_id}}<br/>
          Records: {{ p_accounts_total }}
          {% if p_accounts_has_double %}<br /><span class="warning">There are only {{ p_accounts_distinct }} distinct records!</span> {% endif %}
        </div>
        <div class="pure-control-group">
          <input class="pure-button" type="submit" value="Add"></input>
          {{ p_form.account_id }}
        </div>
        <div class="table-responsive">
          <table class="mq-table pure-table pure-table-bordered">
            <thead>
              <tr>
                <td>#</td>
                <td>Name</td>
                <td>Description</td>
                <td>Active?</td>
                <td>Date created</td>
                <td>Date modified</td>
                <td></td>
              </tr>
            </thead>
            <tbody>
  {% for account in p_accounts %}
<tr><td colspan="7">{{p_form.account_id}}/{{account.account_id}}</td></tr>
    {% if (p_form.account_id > 0) and (p_form.account_id == account.account_id)%}
              <tr>
                <td>{{account.account_id}}/{{ p_form.account_id}}</td>
                <td>{{ p_form.name }}</td>
                <td> {{ p_form.description }}</td>
                <td>{{ p_form.is_active }}</td>
                <td>{{ p_form.date_modified }}</td>
                <td>{{ p_form.date_created }}</td>
                <td>
                  <input class="pure-button" type="submit" value="S"></input> <input class="pure-button" type="submit" value="C"></input>  
                </td>
              </tr>
    {% else %}
              <tr>
                <td>{{ account.account_id }}<input id="account_id" name="account_id" type="hidden" value="{{account.account_id}}"></td>
                <td>{{ account.name }}{{ p_form.name }}</td>
                <td>{{ account.description }}</td>
                <td>{% if account.is_active %}&#9745;{% else %}&#9744;{% endif %}</td>
                <td>{{ account.date_created }}</td>
                <td>{{ account.date_modified }}</td>
                <td>
      {% if not account_id %}
                  <input class="pure-button" type="submit" value="M"></input> <input class="pure-button" type="submit" value="D"></input>  
      {% endif %}
                </td>
              </tr>
    {% endif %}
  {% endfor %}
            </tbody>
          </table>
        </div>
      </fieldset>
    </form>
  </p>
  {% endblock %}
