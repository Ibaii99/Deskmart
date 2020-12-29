import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Injectable({
  providedIn: 'root'
})
export class NotificationsService {

  constructor(private toastr: ToastrService) { }

  showNotification(from, align, type, tittle, message) {
    switch (type) {
      case "info":
        this.toastr.info(
        '<span data-notify="icon" class="nc-icon nc-bell-55"></span><span data-notify="message"><b>'+ tittle +' </b> '+message+'</span>',
          "",
          {
            timeOut: 4000,
            closeButton: true,
            enableHtml: true,
            toastClass: "alert alert-info alert-with-icon",
            positionClass: "toast-" + from + "-" + align
          }
        );
        break;
      case "success":
        this.toastr.success(
          '<span data-notify="icon" class="nc-icon nc-bell-55"></span><span data-notify="message"><b>'+ tittle +' </b> '+message+'</span>',
          "",
          {
            timeOut: 4000,
            closeButton: true,
            enableHtml: true,
            toastClass: "alert alert-success alert-with-icon",
            positionClass: "toast-" + from + "-" + align
          }
        );
        break;
      case "warning":
        this.toastr.warning(
        '<span data-notify="icon" class="nc-icon nc-bell-55"></span><span data-notify="message"><b>'+ tittle +' </b> '+message+'</span>',
          "",
          {
            timeOut: 4000,
            closeButton: true,
            enableHtml: true,
            toastClass: "alert alert-warning alert-with-icon",
            positionClass: "toast-" + from + "-" + align
          }
        );
        break;
      case "error":
        this.toastr.error(
        '<span data-notify="icon" class="nc-icon nc-bell-55"></span><span data-notify="message"><b>'+ tittle +' </b> '+message+'</span>',
          "",
          {
            timeOut: 4000,
            enableHtml: true,
            closeButton: true,
            toastClass: "alert alert-danger alert-with-icon",
            positionClass: "toast-" + from + "-" + align
          }
        );
        break;
      case "show":
        this.toastr.show(
        '<span data-notify="icon" class="nc-icon nc-bell-55"></span><span data-notify="message"><b>'+ tittle +' </b> '+message+'</span>',
          "",
          {
            timeOut: 4000,
            closeButton: true,
            enableHtml: true,
            toastClass: "alert alert-primary alert-with-icon",
            positionClass: "toast-" + from + "-" + align
          }
        );
        break;
      default:
        break;
    }
  }

}
