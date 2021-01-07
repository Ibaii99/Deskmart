import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthorizationService } from 'app/services/Auth/authorization.service';
import { NotificationsService } from 'app/services/Notification/notifications.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html'
})
export class LogoutComponent implements OnInit {
  noti: NotificationsService;

  constructor(private router:Router, private backend: AuthorizationService, private toastr: ToastrService) {
    this.noti = new NotificationsService(this.toastr);
  }


  ngOnInit(): void {
    this.noti.showNotification('top', 'right', "info", "Logging Out", "You will be redirect in few seconds.");

    this.backend.logout().then(
      (user) => {
        console.log(user);
        if (localStorage.token) {
          localStorage.clear();
          localStorage.removeItem('token');
          this.router.navigate(['login']);
        }
        else {
        }
      }
    );
  }



}
