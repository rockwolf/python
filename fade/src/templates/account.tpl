{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/account/" method="post" name="FormAccount" class="pure-form pure-form-aligned">
      {{ p_form.hidden_tag() }}
      <fieldset>
        <div class="pure-control-group">
          Records: {{ p_accounts_total }}
          {% if p_accounts_has_double %} <span class="warning">There are only {{ p_accounts_distinct }} distinct records!</span> {% endif %}
        </div>
        <!--div class="pure-control-group"-->
          <table class="pure-table pure-table-bordered">
            <thead>
              <tr>
                <td>#</td>
                <td>Name</td>
                <td>Description</td>
                <td>Active?</td>
                <td>Date created</td>
                <td>Date modified</td>
              </tr>
            </thead>
            <tbody>
              {% for account in p_accounts %}
              <tr>
                <td>{{ account.account_id }}</td>
                <td>{{ p_form.p_account_name }} {{ account.name }}</td> <!-- how to load the second account.name into the input text from p_form.p_account_name? -->
                <td>{{ account.description }}</td>
                <td><input class="pure-checkbox" type="checkbox" {% if account.is_active %}checked {% endif %}/></td>
                <td>{{ account.date_created }}</td>
                <td>{{ account.date_modified }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        <!--/div-->
        <div class="pure-control-group">
          <input class="pure-button" type="submit" value="Add"></input>
          <input class="pure-button" type="submit" value="Modify"></input>
          <input class="pure-button" type="submit" value="Delete"></input>
       </div>
      </fieldset>
    </form>
  </p>
   if p_account_changed 
  <p>New account info saved.</p>
   endif 
{% endblock %}
