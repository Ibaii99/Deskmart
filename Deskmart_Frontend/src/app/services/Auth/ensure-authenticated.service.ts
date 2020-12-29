import { Injectable } from '@angular/core';
import { CanActivate, Router} from '@angular/router';
import { AuthorizationService } from './authorization.service';

@Injectable({
  providedIn: 'root'
})
export class EnsureAuthenticatedService implements CanActivate{

  constructor(private auth: AuthorizationService, private router:Router) { }

  canActivate(): boolean {
    if (localStorage.getItem('token')) {
      return true;
    }
    else {
      this.router.navigateByUrl('login');
      return false;
    }
  }
}
