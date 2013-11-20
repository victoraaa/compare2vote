(function () {
    window.EditPollViewModel = function(kwargs) {
        this.ui = kwargs.ui;
        this.addOptionEndpoint = kwargs.addOptionEndpoint;
        this.title = ko.observable();
        this.question = ko.observable();
        this.newOptionName = ko.observable();
        this.newOptionUrl = ko.observable();
        this.correctPassword = ko.observable();
        this.password = ko.observable();
    };

    EditPollViewModel.prototype = {
        init: function(poll) {
            this.title(poll.title);
            this.question(poll.question);
            this.correctPassword(poll.password);
            ko.applyBindings(this, this.ui.get(0));
        },

        addOption: function() {
            if (this.password() != this.correctPassword() && this.correctPassword()){
                alert("password incorreto!");
                return;
            }
            $.ajax({
                url: this.addOptionEndpoint,
                type: "POST",
                dataType: "json",
                data: {json: JSON.stringify(this.toJSON())},
                traditional: true,
                complete: function(redirect_url) {
                    window.location = redirect_url.responseText;
                },
            });
        },

        toJSON: function() {
            return {
                title: this.title(),
                question: this.question(),
                option: {name: this.newOptionName(), image_url: this.newOptionUrl()}
            };
        },
    };

}) ();
