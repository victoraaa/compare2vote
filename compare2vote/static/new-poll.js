(function () {
    window.NewPollViewModel = function(kwargs) {
        this.ui = kwargs.ui;
        this.createRankingEndpoint = kwargs.createRankingEndpoint;
        this.title = ko.observable();
        this.question = ko.observable();
        this.option1name = ko.observable();
        this.option1url = ko.observable();
        this.option2name = ko.observable();
        this.option2url = ko.observable();
    };

    NewPollViewModel.prototype = {
        init: function(polls) {
            ko.applyBindings(this, this.ui.get(0));
        },

        createRanking: function() {
            $.ajax({
                url: this.createRankingEndpoint,
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
                options: [
                    {name: this.option1name(), image_url: this.option1url()},
                    {name: this.option2name(), image_url: this.option2url()}
                ]
            };
        },
    };

}) ();
