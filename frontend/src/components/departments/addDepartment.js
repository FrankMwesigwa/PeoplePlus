import React, { Component } from 'react';
import axios from 'axios'

class AddDepartment extends Component {

  state = {
      name:'',
      location:''
    };

  handleChange = (e) => {
    this.setState({
        [e.target.name]: e.target.value
    });
  }

  handleSubmit = (e) => {
      e.preventDefault();
        axios.post('http://127.0.0.1:5000/department', this.state )
            .then(response => {
                console.log(response.data);
                this.props.history.push('/departments')
            })

	}

    render() {
        return (

    <div>

            
              <div class="box box-warning">
                
                <div class="box-body">
                <form className="white" onSubmit={this.handleSubmit}>
                <div class="form-group">
                  <label>Department Name</label>
                  <input type="text" class="form-control" name="name" value ={this.state.name} onChange={this.handleChange} placeholder="Enter Branch Name"/>
                </div>

                <div class="form-group">
                  <label>Location</label>
                  <input type="text" class="form-control" name="location" value ={this.state.location} onChange={this.handleChange} placeholder="Enter Branch Location"/>
                </div>

                <div class="footer">
                    <button className="btn btn-primary">Add New  Department</button>
              </div>

                </form>
                </div>
              </div>
    
    </div>
        );
    }
}

export default AddDepartment;

