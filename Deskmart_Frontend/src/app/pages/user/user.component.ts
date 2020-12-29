import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthorizationService } from 'app/services/Auth/authorization.service';
import { map } from 'jquery';
@Component({
    selector: 'user-cmp',
    templateUrl: 'user.component.html',
    styleUrls: ['user.component.scss']
})

export class UserComponent {
  formGroup: FormGroup;

  constructor(private fb: FormBuilder, private backend: AuthorizationService, private router:Router) {
    this.formGroup = fb.group({
      username: new FormControl('', Validators.required),
      email: new FormControl('', Validators.required),
      // password: new FormControl('', Validators.required),
      // confirm_password: new FormControl('', Validators.required),
      first_name: new FormControl('', Validators.required),
      last_name: new FormControl('', Validators.required),
      address: new FormControl(''),
      city: new FormControl(''),
      country: new FormControl(''),
      postal_code: new FormControl(''),
      about: new FormControl('')
    });

   }

  ngOnInit(): void {
    this.backend.description().then(
      (info) => {
        var json = JSON.parse(info);
        console.log(json);
        this.formGroup.controls.username.setValue(json.username);
        this.formGroup.controls.email.setValue(json.email);
        this.formGroup.controls.first_name.setValue(json.first_name);
        this.formGroup.controls.last_name.setValue(json.last_name);
        this.formGroup.controls.address.setValue(json.address);
        this.formGroup.controls.city.setValue(json.city);
        this.formGroup.controls.country.setValue(json.country);
        this.formGroup.controls.postal_code.setValue(json.postal_code);
        this.formGroup.controls.about.setValue(json.about);
      });


  }


  onModify() {
    this.backend.update(this.formGroup.getRawValue()).then(
      (user) => {
        console.log(user);
        localStorage.setItem('token', user.Authorization);
        if (localStorage.token) {
          console.log(localStorage.token);
        }
        else {
        }
      }
    );

  }

  samePasswor(formGroup: FormGroup) {
    return formGroup.get('password').value === formGroup.get('confirm_password').value ? null : { notSame: true }
  }


}
