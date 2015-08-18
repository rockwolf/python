{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/account/" method="post" name="FormAccount">
      {{ p_form.hidden_tag() }}
      {% for account in p_accounts %}
      <table>
        <tr>
          <td>{{ account.name }}</td>
          <td>&nbsp;</td>
          <td>{{ account.description }}</td>
          <td>&nbsp;</td>
          <td><input class="pure-checkbox" type="checkbox" {% if account.is_active %}checked {% endif %}/></td>
          <td>&nbsp;</td>
          <td>{{ account.date_created }}</td>
          <td>&nbsp;</td>
          <td>{{ account.date_modified }}</td>
        </tr>
      </table>
      {% endfor %}
      {{ p_form.p_account }}
      <p>
        <input class="pure-button" type="submit" value="Add"></input>
        <input class="pure-button" type="submit" value="Modify"></input>
        <input class="pure-button" type="submit" value="Delete"></input>
     </p>
    </form>
  </p>
   if p_account_changed 
  <p>New account info saved.</p>
   endif 
{% endblock %}
