import React, {Component} from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

import AddIssue from './components/issues/addIssue';
import IssueDetail from './components/issues/issueDetails';
import IssuesList from './components/issues/issuesList';
import EditIssue from './components/issues/editIssue';

class App extends Component {
  render () {
    return (
      <BrowserRouter>
        <div className="container">
          <div>
            <Switch>
              <Route exact path="/" Component={IssuesList} />
              <Route exact path="/add" Component={AddIssue} />
              <Route exact path="/issue/:id" Component={IssueDetail} />;
              <Route exact path="/edit/:id" Component={EditIssue} />;

            </Switch>
          </div>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
