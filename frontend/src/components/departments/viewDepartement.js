import React, { Component } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

class ViewDepartment extends Component {

    state = {
        ViewDepartment: {}
  } 

  componentDidMount = () => {
        const id = this.props.match.params.id
        axios.get('http://127.0.0.1:5000/branch/'+id)
            .then(response => {
                this.setState({branch: response.data});
                console.log(response);
            })
            .catch(error => {
                this.setState({error:true})
        });
}

  handleDelete = (id) => {
    axios.delete('http://127.0.0.1:5000/branch/'+id)
      .then(result => {
        this.props.history.push('/branches')
      });
  }

  render() {
    return (
      <div class="container">
        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">
              {this.state.department.name}
            </h3>
          </div>
          <div class="panel-body">
            <h4><Link to="/departments"><span class="glyphicon glyphicon-th-list" aria-hidden="true"></span> Department List</Link></h4>
            <dl>
              <dt>department ID:</dt>
              <dd>{this.state.branch.id}</dd>
              <dt>Department Name:</dt>
              <dd>{this.state.department.name}</dd>
              <dt>Department Location:</dt>
              <dd>{this.state.department.location}</dd>
            </dl>
            <Link to={'/departmentedit/${this.state.branch.id}'} class="btn btn-primary">Edit Department</Link>&nbsp;
            <button onClick={ ()=> this.handleDelete(this.state.ViewDepartment.id) } class="btn btn-danger">Delete Department</button>           
          </div>

        </div>
      </div>
    );
  }
}

export default ViewDepartment;
