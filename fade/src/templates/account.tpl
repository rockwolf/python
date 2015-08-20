{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/account/" method="post" name="FormAccount" class="pure-form pure-form-aligned">
      {{ p_form.hidden_tag() }}
      <fieldset>
        <div class="pure-control-group">
          Records: {{ p_accounts_total }}
          {% if p_accounts_has_double %}<br /><span class="warning">There are only {{ p_accounts_distinct }} distinct records!</span> {% endif %}
        </div>
        <div class="pure-control-group">
          <input class="pure-button" type="submit" value="Add"></input>
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
              <!-- test on if account.name = p_form_account.name (obj)-->
              <!-- if equal then show row with edits -->
              {% if  p_account_name != account.name %}
              <tr>
                <td> Yeeeeeaaaah!</td>
                <td>{{ p_form.p_account_name }}</td>
                <td> Yeeeeeaaaah!</td>
                <td><input class="pure-checkbox" type="checkbox" readonly {% if account.is_active %}checked {% endif %}/></td>
                <td> Yeeeeeaaaah!</td>
                <td> Yeeeeeaaaah!</td>
                <td>
                  <input class="pure-button" type="submit" value="Modify"></input> <input class="pure-button" type="submit" value="Delete"></input>  
                </td>
              </tr>
              {% else %}
              <tr>
                <td>{{ account.account_id }}</td>
                <td>{{ account.name }}</td>
                <td>{{ account.description }}</td>
                <td><input class="pure-checkbox" type="checkbox" readonly {% if account.is_active %}checked {% endif %}/></td>
                <td>{{ account.date_created }}</td>
                <td>{{ account.date_modified }}</td>
                <td>
                  <input class="pure-button" type="submit" value="Modify"></input> <input class="pure-button" type="submit" value="Delete"></input>  
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
   if p_account_changed 
  <p>New account info saved.</p>
   endif 
{% endblock %}
