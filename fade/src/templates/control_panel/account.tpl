{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="{{url_for('control_panel.render_account', account_id=p_form.data.account_id) }}" method="post" name="FormAccount" class="pure-form pure-form-aligned">
      {{ p_form.hidden_tag() }}
      <fieldset>
        <div class="pure-control-group">
    p_form.account_id: {{p_form.account_id}}<br/>
    p_account_id: {{p_account_id}}<br/>
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
<tr><td colspan="7">{{ p_account_id }}/{{ account.account_id }}/{{ p_form.data.account_id }}</td></tr>
    {% if (account.account_id == p_account_id) %}
              <tr>
                <td>{{ account.account_id }}/{{ p_form.data.account_id }}</td>
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
    <!-- This part is default. when pressing modify, I have the action = p_form.data.account_id. But that gives many results. How to specify the one from the line where the button is pressed? -->
    <!-- One option is to put the hidden field somewhere and fill it with javascript. But I don't like that method. Isn't there a better way? -->
    <!-- Note: perhaps change the id of the hidden input, to account_id{{account.account_id}} and do a request.form['account_id'+account_id]
     where account_id = the damn ID we are trying to figure out! Dammit! -->
    <!-- Note: Ah, this guy cheats by not using a form: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends -->
              <tr>
                <td>{{ account.account_id }}</td>
                <td>{{ account.name }}</td>
                <td>{{ account.description }}</td>
                <td>{% if account.is_active %}&#9745;{% else %}&#9744;{% endif %}</td>
                <td>{{ account.date_created }}</td>
                <td>{{ account.date_modified }}</td>
                <td>
      {% if not account_id %}
                  <a href="{{url_for('control_panel.render_account', account_id=account.account_id) }}"><input class="pure-button" value="M"></input></a> <input class="pure-button" type="submit" value="D"></input>  
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
