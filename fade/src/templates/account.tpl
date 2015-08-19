{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/account/" method="post" name="FormAccount">
      {{ p_form.hidden_tag() }}
      <p>
        <input class="pure-button" type="submit" value="Add"></input>
        <input class="pure-button" type="submit" value="Modify"></input>
        <input class="pure-button" type="submit" value="Delete"></input>
     </p>
     <p>Total/distinct: {{ p_accounts_total }}/{{ p_accounts_distinct }}</p>
      {% for account in p_accounts %}
      <table class="pure-table pure-table-bordered pure-table-striped">
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
          <tr>
            <td>{{ account.account_id }}</td>
            <td>{{ p_form.p_account_name }} {{ account.name }}</td> <!-- how to load the second account.name into the input text from p_form.p_account_name? -->
            <td>{{ account.description }}</td>
            <td><input class="pure-checkbox" type="checkbox" {% if account.is_active %}checked {% endif %}/></td>
            <td>{{ account.date_created }}</td>
            <td>{{ account.date_modified }}</td>
          </tr>
        </tbody>
      </table>
      {% endfor %}
      {{ p_form.p_account }}
    </form>
  </p>
   if p_account_changed 
  <p>New account info saved.</p>
   endif 
{% endblock %}
