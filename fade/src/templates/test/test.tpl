{% extends "base.tpl" %}
{% block body %}
  <p>
    <form action="/test/" method="post" name="FormTest" class="pure-form pure-form-aligned">
      {{ p_form.hidden_tag() }}
      <fieldset>
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
              <tr>
                <td>{{ account.account_id}}</td>
                <td>{{ account.name }}</td>
                <td> {{ account.description }}</td>
                <td>{{ account.is_active }}</td>
                <td>{{ account.date_modified }}</td>
                <td>{{ account.date_created }}</td>
                <td>
                  <a href="{{url_for('test', account_id=account.id)}}">Edit</a>
                  <input class="pure-button" type="submit" value="Edit"></input> <input class="pure-button" type="submit" value="Cancel"></input>  
                </td>
              </tr>
            {% endfor %}
            </tbody>
          </table>
        </div>
      </fieldset>
    </form>
  </p>
  {% endblock %}
