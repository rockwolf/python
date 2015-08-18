{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/account/" method="post" name="FormAccount">
      {{ p_form.hidden_tag() }}
      {{ p_form.p_account }} # TODO: this form only on add? What about delete?
      {% for account in p_form.p_accounts %}
      <table>
        <tr>
          <td>{{ account.name }}</td>
          <td>{{ account.description }}</td>
          <td><input class="pure-checkbox" type="checkbox" {% if account.is_active %}checked {% endif %}/></td>
          <td>{{ account.date_created }}</td>
          <td>{{ account.date_modified }}</td>
        </tr>
      </table>
      {% endfor %}
      <p>
        <input class="pure-button" type="submit" value="Add"></input>
        <input class="pure-button" type="submit" value="Modify"></input>
        <input class="pure-button" type="submit" value="Delete"></input>
     </p>
    </form>
  </p>
  {% if p_account_changed %}
  <p>New account info saved.</p>
  {% endif %}
{% endblock %}
