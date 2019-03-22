import React, { Component } from 'react';
import axios from 'axios';

class EditDepartment extends Component {

  state = {
      department: {}
}

  componentDidMount = () => {
    const id = this.props.match.params.id
    axios.get('http://127.0.0.1:5000/branch/'+id)
    .then(response => {
      this.setState({ department: response.data });
      console.log(this.state.department);
    });
  }

  handleChange = (e) => {
    const state = this.state.department
    state[e.target.name] = e.target.value;
    this.setState({department:state});
  }

  handleSubmit = (e) => {
    e.preventDefault();
    const id = this.props.match.params.id
    const { name, location } = this.state.department;

    axios.put('http://127.0.0.1:5000/branch/'+id, { name, location })
      .then(result => {
        console.log(result.data)
        this.props.history.push('/branch/'+id)
      });
  }

  render() {
    return (
        <div>

            
        <div class="box box-warning">
          
          <div class="box-body">
          <form className="white" onSubmit={this.handleSubmit}>
          <div class="form-group">
            <label>Department Name</label>
            <input type="text" class="form-control" name="name" value ={this.state.branch.name} onChange={this.handleChange} placeholder="Enter Branch Name"/>
          </div>

          <div class="form-group">
            <label>Department Location</label>
            <input type="text" class="form-control" name="location" value ={this.state.branch.location} onChange={this.handleChange} placeholder="Enter Branch Location"/>
          </div>

          <div class="footer">
              <button type="submit" className="btn btn-success">Edit Department</button>
        </div>

          </form>
          </div>
        </div>

</div>
    );
  }
}

export default EditDepartment;